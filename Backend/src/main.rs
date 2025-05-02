use actix_web::{App, get, HttpResponse, HttpServer};
use cooklang::CooklangParser;
use std::{fs::File, io::{self, Read}};

#[get("/")]
async fn hello() -> HttpResponse{
    HttpResponse::Ok().body("<h1>Backend Running</h1>")
}

fn read_file() -> String{
    let mut recipe_file = File::open("./recipes-main/Baking/Beer Bread.cook").ok().expect("Failed to find file");
    let mut recipe_string = String::new();

    recipe_file.read_to_string(&mut recipe_string).ok().expect("Could not read file");

    recipe_string

}

#[actix_web::main]
async fn main() -> std::io::Result<()>{
    let recipe_text = read_file();
    let parser = CooklangParser::default();

    let (recipe, _warnings) = parser.parse(&recipe_text).into_result().ok().expect("could not parse your bullshit");

    println!("first recipe ingredient is {}", recipe.ingredients[0].name);

    HttpServer::new( ||{App::new()
        .service(hello)
    
    })
        .bind(("localhost", 8170))?
        .run()
        .await    
}
 