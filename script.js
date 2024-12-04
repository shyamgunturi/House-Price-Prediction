document.getElementById("predictForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    // Collect input values from the form
    const squareFeet = document.getElementById("squareFeet").value;
    const bedrooms = document.getElementById("bedrooms").value;
    const bathrooms = document.getElementById("bathrooms").value;
    const proximity = document.getElementById("proximity").value;
  
    // Send data to the backend in JSON format
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        squareFeet: Number(squareFeet), // Convert to number before sending
        bedrooms: Number(bedrooms),
        bathrooms: Number(bathrooms),
        proximity: Number(proximity),
      }),
    });
  
    const result = await response.json(); // Parse the result
    document.getElementById("result").innerText = `Predicted Price: ₹${result.price}`;
  });
  