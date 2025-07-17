<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Email Spam Classifier</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background: #f4f4f4;
    }
    h2 {
      color: #333;
    }
    textarea {
      width: 100%;
      height: 100px;
      margin-bottom: 10px;
      font-size: 14px;
    }
    button {
      padding: 10px 20px;
      background-color: #28a745;
      color: white;
      border: none;
      cursor: pointer;
      margin-bottom: 20px;
    }
    button:hover {
      background-color: #218838;
    }
    .result {
      background: #fff;
      padding: 10px;
      margin-top: 10px;
      border-left: 4px solid #28a745;
    }
  </style>
</head>
<body>

  <h2>Spam Email Classifier</h2>

  <p>Enter email content (you can enter multiple emails, one per line):</p>
  <textarea id="emailInput" placeholder="Enter one or more emails here..."></textarea>
  <br>
  <button onclick="submitEmails()">Submit</button>

  <div id="results"></div>

  <script>
    async function submitEmails() {
      const inputText = document.getElementById("emailInput").value;
      const emails = inputText.split("\n").filter(line => line.trim() !== "");

      const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ emails })
      });

      const results = await response.json();

      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = "";

      results.forEach((res, index) => {
        const div = document.createElement("div");
        div.className = "result";
        div.innerText = Email ${index + 1}: ${res.result};
        resultsDiv.appendChild(div);
      });
    }
  </script>

</body>
</html>