async function sendMessage() {
  const input = document.getElementById("user-input");
  const msg = input.value.trim();
  const chatBox = document.getElementById("chat-box");
  const model = document.getElementById("model-select").value;

  if (!msg) return;

  chatBox.innerHTML += `<p><strong>You:</strong> ${msg}</p>`;

  try {
    const res = await fetch(`https://smeher.pythonanywhere.com${model}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });

    const data = await res.json();
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    chatBox.innerHTML += `<p><strong>Bot:</strong> Oops! Server error.</p>`;
  }

  input.value = "";
}
