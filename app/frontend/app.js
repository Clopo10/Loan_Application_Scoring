// 1. Listen for the user clicking the Submit button
document
  .getElementById("loanForm")
  .addEventListener("submit", async function (event) {
    // Stop the page from refreshing when the button is clicked
    event.preventDefault();

    // 2. Gather the numbers from the HTML text boxes
    const applicationData = {
      age: parseInt(document.getElementById("age").value),
      income: parseFloat(document.getElementById("income").value),
      loan_amount: parseFloat(document.getElementById("loan_amount").value),
      credit_score: parseInt(document.getElementById("credit_score").value),
    };

    try {
      // 3. Send the JSON to your Python backend using fetch()
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(applicationData),
      });

      // 4. Wait for Python to reply, and read the result
      const result = await response.json();

      // 5. Update the screen with the results!
      const resultBox = document.getElementById("resultBox");
      const displayScore = document.getElementById("displayScore");
      const displayCategory = document.getElementById("displayCategory");

      displayScore.textContent = result.risk_score;
      if (result.risk_category === "LOW") {
        displayCategory.textContent = "Approved";
      } else if (result.risk_category === "MEDIUM") {
        displayCategory.textContent = "Flagged for Review";
      } else {
        displayCategory.textContent = "Denied";
      }

      // Change color based on the category
      if (result.risk_score >= 70) {
        resultBox.className =
          "mt-6 p-4 rounded-md bg-green-100 text-green-800 block";
      } else if (30 < result.risk_score && result.risk_score < 70) {
        resultBox.className =
          "mt-6 p-4 rounded-md bg-yellow-100 text-yellow-800 block";
      } else {
        resultBox.className =
          "mt-6 p-4 rounded-md bg-red-100 text-red-800 block";
      }
    } catch (error) {
      alert("Failed to connect to the API. Is your Uvicorn server running?");
      console.error("API Error:", error);
    }
  });
