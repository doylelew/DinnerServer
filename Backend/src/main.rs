mod models;

use actix_web::{get, post, App, HttpRequest, HttpResponse, HttpServer};
use cooklang::{CooklangParser, ScalableRecipe};
use std::{fs::File, io::{self, Read}};


fn read_file(file: File) -> String{
    let mut recipe_file = file;
    let mut recipe_string = String::new();

    recipe_file.read_to_string(&mut recipe_string).ok().expect("Could not read file");

    recipe_string

}

fn parse_file(recipe_file:File) -> ScalableRecipe {
    let recipe_text = read_file(recipe_file);
    let parser = CooklangParser::default();

    let (recipe, _warnings) = parser.parse(&recipe_text).into_result().ok().expect("could not parse your bullshit");
    recipe
}

fn parse_string(recipe_text: String) -> ScalableRecipe {
    let parser = CooklangParser::default();

    let (recipe, _warnings) = parser.parse(&recipe_text).into_result().ok().expect("could not parse your bullshit");
    recipe
}

#[post("/upload_recipe")]
async fn upoload_recipe(response: String) -> HttpResponse{

    let recipe_object = parse_string(response);
    HttpResponse::Ok().json(recipe_object)
}

#[get("/")]
async fn endpoints() -> HttpResponse{
    HttpResponse::Ok().body("<h1>Enpoints</h1>")
}

#[actix_web::main]
async fn main() -> std::io::Result<()>{
   
    HttpServer::new( ||{App::new()
        .service(endpoints)
        .service(upoload_recipe)
    
    })
        .bind(("localhost", 8170))?
        .run()
        .await    
}
 