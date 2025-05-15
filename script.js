function getBotResponse(input) {
  return fetch("https://smeher.pythonanywhere.com/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: input })
  })
    .then(res => res.json())
    .then(data => data.response)
    .catch(() => "Oops! Server error.");
}

async function sendMessage() {
  const input = document.getElementById("user-input").value;
  const chatBox = document.getElementById("chat-box");

  chatBox.innerHTML += `<p><strong>You:</strong> ${input}</p>`;

  const botReply = await getBotResponse(input);
  chatBox.innerHTML += `<p><strong>Bot:</strong> ${botReply}</p>`;

  document.getElementById("user-input").value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}
