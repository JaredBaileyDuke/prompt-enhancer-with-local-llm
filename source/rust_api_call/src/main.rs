use actix_web::{post, web, App, HttpServer, Responder, HttpResponse};
use reqwest::Client;
use serde::{Deserialize, Serialize};
use serde_json::json;
use std::error::Error;
use log::{info, error};
use std::time::Instant;

#[derive(Serialize)]
struct Message {
    role: String,
    content: String,
}

#[derive(Deserialize)]
struct Choice {
    message: MessageContent,
}

#[derive(Deserialize)]
struct MessageContent {
    content: String,
}

#[derive(Deserialize)]
struct CompletionResponse {
    choices: Vec<Choice>,
}

#[derive(Deserialize)]
struct LlmRequest {
    system_message: String,
    user_message: String,
}

async fn llm_message(system_message: &str, user_message: &str) -> Result<String, Box<dyn Error>> {
    let client = Client::new();
    let api_key = "sk-no-key-required";
    let url = "http://localhost:8080/v1/chat/completions";

    let messages = [
        Message {
            role: "system".to_string(),
            content: system_message.to_string(),
        },
        Message {
            role: "user".to_string(),
            content: user_message.to_string(),
        },
    ];

    let body = json!({
        "model": "LLaMA_CPP",
        "messages": messages,
    });

    info!("Sending request to LLM API");
    let start = Instant::now();

    let response = client
        .post(url)
        .bearer_auth(api_key)
        .json(&body)
        .send()
        .await?;

    let response_time = start.elapsed();
    info!("Received response from LLM API in {:?}", response_time);

    let completion_response_start = Instant::now();
    let completion_response = response.json::<CompletionResponse>().await?;
    let parsing_time = completion_response_start.elapsed();
    info!("Parsed response from LLM API in {:?}", parsing_time);

    let total_time = start.elapsed();
    info!("Total time for llm_message: {:?}", total_time);

    Ok(completion_response.choices.get(0).map_or("".to_string(), |choice| choice.message.content.clone()))
}

#[post("/llm_message")]
async fn llm_message_handler(req: web::Json<LlmRequest>) -> impl Responder {
    info!("Handling request");
    let handler_start = Instant::now();
    let result = llm_message(&req.system_message, &req.user_message).await;
    let handler_time = handler_start.elapsed();
    info!("llm_message_handler completed in {:?}", handler_time);
    
    match result {
        Ok(content) => {
            info!("Returning content to client");
            HttpResponse::Ok().body(content)
        },
        Err(e) => {
            error!("Error occurred: {:?}", e);
            HttpResponse::InternalServerError().body("Error occurred")
        },
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();
    info!("Starting server at http://127.0.0.1:8081");

    HttpServer::new(|| {
        App::new()
            .service(llm_message_handler)
    })
    .bind("127.0.0.1:8081")?
    .run()
    .await
}
