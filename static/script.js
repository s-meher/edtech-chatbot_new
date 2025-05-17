function sendMessage() {
  const input = document.getElementById("user-input").value;
  const chatBox = document.getElementById("chat-box");

  const userMessage = `<p><strong>You:</strong> ${input}</p>`;
  chatBox.innerHTML += userMessage;

  fetch("https://smeher.pythonanywhere.com/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: input })
  })
    .then(response => response.json())
    .then(data => {
      const botReply = `<p><strong>Bot:</strong> ${data.response}</p>`;
      chatBox.innerHTML += botReply;
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
      chatBox.innerHTML += `<p><strong>Bot:</strong> Oops! Server error.</p>`;
    });

  document.getElementById("user-input").value = "";
}
