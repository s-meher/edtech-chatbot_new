async function sendMessage() {
  const input = document.getElementById("user-input").value;
  const model = document.getElementById("model-select").value;
  const chatBox = document.getElementById("chat-box");

  const userMessage = `<p><strong>You:</strong> ${input}</p>`;
  chatBox.innerHTML += userMessage;

  try {
    const res = await fetch(model, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input })
    });
    const data = await res.json();
    const botReply = `<p><strong>Bot:</strong> ${data.response}</p>`;
    chatBox.innerHTML += botReply;
  } catch (error) {
    chatBox.innerHTML += `<p><strong>Bot:</strong> Error contacting server.</p>`;
  }

  chatBox.scrollTop = chatBox.scrollHeight;
  document.getElementById("user-input").value = "";
}
