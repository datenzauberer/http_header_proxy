#![deny(warnings)]

use std::convert::Infallible;
use std::net::SocketAddr;
use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Client, Request, Response, Server};
use hyper_tls::HttpsConnector;


#[tokio::main]
async fn main() {
    let addr = SocketAddr::from(([127, 0, 0, 1], 8100));

    let https = HttpsConnector::new();
    let client = Client::builder()
        .http1_title_case_headers(true)
        .http1_preserve_header_case(true)
        .build::<_, hyper::Body>(https);

    let make_service = make_service_fn(move |_| {
        let client = client.clone();
        async move { Ok::<_, Infallible>(service_fn(move |req| proxy_remove_body(client.clone(), req))) }
    });

    let server = Server::bind(&addr)
        .http1_preserve_header_case(true)
        .http1_title_case_headers(true)
        .serve(make_service);

    println!("Listening on http://{}", addr);

    if let Err(e) = server.await {
        eprintln!("server error: {}", e);
    }
}

async fn proxy_remove_body(
    client: Client<HttpsConnector<hyper::client::HttpConnector>>,
    req: Request<Body>
) -> Result<Response<Body>, hyper::Error> {
    let headers = req.headers().clone();
    println!("headers: {:?}", headers);

    let mut response = client.request(req).await?;
    // just remove the
    *response.body_mut() = Body::from("");
    Ok(response)
}
