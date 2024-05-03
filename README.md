## Flask Application Design

### HTML Files

- **index.html:** The main page of the application where the user enters the property address and uploads the photos.
- **result.html:** The page that displays the estimated value, confidence level, market analysis, and comparable properties.

### Routes

- **/:** The route for the main page.
- **/validate_address:** The route that validates the provided address against Google Maps.
- **/upload_photos:** The route that handles the upload of interior and exterior photos.
- **/generate_estimate:** The route that processes the provided information and generates an estimated value for the property.

### Detailed Explanation

1. The user accesses the application through the **index.html** page.
2. The user enters the property address and clicks on the "Validate" button, which triggers a request to the **/validate_address** route.
3. The **/validate_address** route validates the address against Google Maps and returns a message to the user, indicating whether the address is valid or not.
4. If the address is valid, the user can upload interior and exterior photos of the property by clicking on the "Upload Photos" button, which triggers a request to the **/upload_photos** route.
5. The **/upload_photos** route processes the uploaded photos and saves them to the server.
6. Once the photos are uploaded, the user can click on the "Generate Estimate" button, which triggers a request to the **/generate_estimate** route.
7. The **/generate_estimate** route uses the provided address and photos to generate an estimated value for the property.
8. The estimated value, confidence level, market analysis, and comparable properties are displayed on the **result.html** page.