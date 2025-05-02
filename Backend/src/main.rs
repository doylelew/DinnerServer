use actix_web::{App, get, HttpResponse, HttpServer};

#[get("/")]
async fn hello() -> HttpResponse{
    HttpResponse::Ok().body("<h1>Backend Running</h1>")
}

#[actix_web::main]
async fn main() -> std::io::Result<()>{
    HttpServer::new( ||{App::new()
        .service(hello)
    
    })
        .bind(("localhost", 8170))?
        .run()
        .await    
}
 