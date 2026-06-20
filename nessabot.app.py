import streamlit as module
module.set_page_config(page_title="NessaBot — Know God")

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NessaBot — Know God</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>
  :root {
    --gold: #c9a84c;
    --gold-light: #f0d080;
    --gold-dim: #7a601e;
    --deep: #0d0a06;
    --parchment: #f7f0e0;
    --warm: #1a1208;
    --glow: rgba(201,168,76,0.18);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--deep);
    font-family: 'Lora', serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
  }

  /* Starfield background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
      radial-gradient(ellipse at 20% 20%, rgba(201,168,76,0.06) 0%, transparent 50%),
      radial-gradient(ellipse at 80% 80%, rgba(201,168,76,0.04) 0%, transparent 50%),
      radial-gradient(ellipse at 50% 0%, rgba(201,168,76,0.08) 0%, transparent 40%);
    pointer-events: none;
    z-index: 0;
  }

  /* Particle stars */
  .stars {
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
  }
  .star {
    position: absolute;
    width: 2px; height: 2px;
    border-radius: 50%;
    background: var(--gold-light);
    animation: twinkle var(--d) ease-in-out infinite alternate;
    opacity: 0;
  }
  @keyframes twinkle {
    from { opacity: 0; transform: scale(0.5); }
    to   { opacity: 0.7; transform: scale(1.2); }
  }

  .container {
    position: relative;
    z-index: 1;
    width: 420px;
    max-width: 96vw;
    display: flex;
    flex-direction: column;
    height: 640px;
    max-height: 94vh;
  }

  /* Header */
  .header {
    text-align: center;
    padding: 20px 0 14px;
    position: relative;
  }
  .header::after {
    content: '';
    display: block;
    margin: 10px auto 0;
    width: 60%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
  }
  .halo {
    width: 64px; height: 64px;
    margin: 0 auto 10px;
    border-radius: 50%;
    background: radial-gradient(circle at 40% 35%, #fff9e0 0%, var(--gold-light) 40%, var(--gold-dim) 100%);
    box-shadow: 0 0 24px 8px rgba(201,168,76,0.45), 0 0 60px 16px rgba(201,168,76,0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    animation: pulse 3s ease-in-out infinite;
  }
  @keyframes pulse {
    0%,100% { box-shadow: 0 0 24px 8px rgba(201,168,76,0.45), 0 0 60px 16px rgba(201,168,76,0.15); }
    50%      { box-shadow: 0 0 36px 14px rgba(201,168,76,0.65), 0 0 80px 24px rgba(201,168,76,0.25); }
  }
  h1 {
    font-family: 'Cinzel Decorative', serif;
    font-size: 1.45rem;
    color: var(--gold-light);
    letter-spacing: 0.08em;
    text-shadow: 0 0 20px rgba(201,168,76,0.5);
  }
  .subtitle {
    font-size: 0.72rem;
    color: var(--gold-dim);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-top: 2px;
  }

  /* Chat window */
  .chat-window {
    flex: 1;
    overflow-y: auto;
    padding: 16px 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(201,168,76,0.15);
    border-radius: 12px;
    scrollbar-width: thin;
    scrollbar-color: var(--gold-dim) transparent;
  }
  .chat-window::-webkit-scrollbar { width: 4px; }
  .chat-window::-webkit-scrollbar-thumb { background: var(--gold-dim); border-radius: 2px; }

  .msg {
    display: flex;
    flex-direction: column;
    max-width: 82%;
    animation: fadeUp 0.35s ease both;
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .msg.bot { align-self: flex-start; }
  .msg.user { align-self: flex-end; }

  .bubble {
    padding: 10px 14px;
    border-radius: 16px;
    font-size: 0.88rem;
    line-height: 1.55;
  }
  .bot .bubble {
    background: linear-gradient(135deg, rgba(201,168,76,0.12), rgba(201,168,76,0.05));
    border: 1px solid rgba(201,168,76,0.25);
    color: var(--parchment);
    border-bottom-left-radius: 4px;
  }
  .user .bubble {
    background: linear-gradient(135deg, var(--gold-dim), #5a4010);
    border: 1px solid rgba(201,168,76,0.3);
    color: var(--parchment);
    border-bottom-right-radius: 4px;
  }
  .sender {
    font-size: 0.65rem;
    color: var(--gold-dim);
    letter-spacing: 0.12em;
    margin-bottom: 3px;
    text-transform: uppercase;
  }
  .msg.user .sender { text-align: right; }

  /* Quick replies */
  .quick-replies {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }
  .qr-btn {
    background: transparent;
    border: 1px solid rgba(201,168,76,0.35);
    color: var(--gold);
    font-family: 'Lora', serif;
    font-size: 0.72rem;
    padding: 4px 10px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.2s;
    letter-spacing: 0.05em;
  }
  .qr-btn:hover {
    background: rgba(201,168,76,0.12);
    border-color: var(--gold);
    box-shadow: 0 0 10px rgba(201,168,76,0.2);
  }

  /* Typing indicator */
  .typing { display: flex; align-items: center; gap: 5px; padding: 6px 0; }
  .typing span {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--gold);
    animation: bounce 1.2s ease-in-out infinite;
    opacity: 0.7;
  }
  .typing span:nth-child(2) { animation-delay: 0.2s; }
  .typing span:nth-child(3) { animation-delay: 0.4s; }
  @keyframes bounce {
    0%,60%,100% { transform: translateY(0); }
    30% { transform: translateY(-6px); opacity: 1; }
  }

  /* Input area */
  .input-area {
    padding: 12px 0 0;
    display: flex;
    gap: 8px;
    align-items: flex-end;
  }
  .input-wrap {
    flex: 1;
    position: relative;
  }
  textarea {
    width: 100%;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(201,168,76,0.25);
    border-radius: 10px;
    padding: 10px 14px;
    color: var(--parchment);
    font-family: 'Lora', serif;
    font-size: 0.88rem;
    resize: none;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    min-height: 44px;
    max-height: 100px;
    line-height: 1.5;
  }
  textarea::placeholder { color: rgba(201,168,76,0.3); font-style: italic; }
  textarea:focus {
    border-color: rgba(201,168,76,0.6);
    box-shadow: 0 0 14px rgba(201,168,76,0.12);
  }

  .send-btn {
    width: 44px; height: 44px;
    border-radius: 10px;
    background: linear-gradient(135deg, var(--gold), var(--gold-dim));
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    flex-shrink: 0;
  }
  .send-btn:hover {
    transform: scale(1.06);
    box-shadow: 0 0 18px rgba(201,168,76,0.5);
  }
  .send-btn svg { width: 18px; height: 18px; fill: var(--deep); }

  /* Divider ornament */
  .ornament {
    text-align: center;
    color: var(--gold-dim);
    font-size: 0.7rem;
    letter-spacing: 0.3em;
    margin: 2px 0;
    opacity: 0.6;
  }
</style>
</head>
<body>

<div class="stars" id="stars"></div>

<div class="container">
  <div class="header">
    <div class="halo">✦</div>
    <h1>NessaBot</h1>
    <p class="subtitle">Seek · Pray · Know</p>
  </div>

  <div class="ornament">✦ ✦ ✦</div>

  <div class="chat-window" id="chatWindow">
    <div class="msg bot" style="animation-delay:0.1s">
      <div class="sender">NessaBot</div>
      <div class="bubble">Hello! I am NessaBot. 🕊️<br>Ask me how to know about God. Type <em>"bye"</em> to exit.</div>
      <div class="quick-replies">
        <button class="qr-btn" onclick="sendQuick('Who is God?')">Who is God?</button>
        <button class="qr-btn" onclick="sendQuick('How do I know God?')">How do I know God?</button>
        <button class="qr-btn" onclick="sendQuick('How long do I need to pray?')">How long to pray?</button>
        <button class="qr-btn" onclick="sendQuick('Where is God?')">Where is God?</button>
      </div>
    </div>
  </div>

  <div class="input-area">
    <div class="input-wrap">
      <textarea id="userInput" placeholder="Ask about God…" rows="1" onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
    </div>
    <button class="send-btn" onclick="sendMessage()">
      <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
    </button>
  </div>
</div>

<script>
  // Stars
  const starsEl = document.getElementById('stars');
  for (let i = 0; i < 80; i++) {
    const s = document.createElement('div');
    s.className = 'star';
    s.style.cssText = `left:${Math.random()*100}%;top:${Math.random()*100}%;--d:${2+Math.random()*4}s;animation-delay:${Math.random()*4}s`;
    starsEl.appendChild(s);
  }

  const responses = {
    "who is god": "God is your Creator and the creator of the universe. He is the Alpha and Omega — the beginning and the end.",
    "who is god?": "God is your Creator and the creator of the universe. He is the Alpha and Omega — the beginning and the end.",
    "how do i know god": "You know God by going to church, reading and studying the Bible, praying daily, and worshipping Him with all your heart.",
    "how do i know god?": "You know God by going to church, reading and studying the Bible, praying daily, and worshipping Him with all your heart.",
    "how long do i need to pray": "You pray daily for 30 minutes and more. There is no ceiling — the more you pray, the closer you draw to Him.",
    "how long do i need to pray?": "You pray daily for 30 minutes and more. There is no ceiling — the more you pray, the closer you draw to Him.",
    "how long to pray": "You pray daily for 30 minutes and more. There is no ceiling — the more you pray, the closer you draw to Him.",
    "how long to pray?": "You pray daily for 30 minutes and more.",
    "where is god": "He is everywhere — Omnipresent. Not a corner of creation exists where God is absent.",
    "where is god?": "He is everywhere — Omnipresent. Not a corner of creation exists where God is absent.",
    "bye": null
  };

  const chatWindow = document.getElementById('chatWindow');

  function appendMsg(text, who, showQuick = false) {
    const div = document.createElement('div');
    div.className = `msg ${who}`;
    div.innerHTML = `<div class="sender">${who === 'bot' ? 'NessaBot' : 'You'}</div><div class="bubble">${text}</div>`;
    if (showQuick) {
      div.innerHTML += `<div class="quick-replies">
        <button class="qr-btn" onclick="sendQuick('Who is God?')">Who is God?</button>
        <button class="qr-btn" onclick="sendQuick('How do I know God?')">How do I know God?</button>
        <button class="qr-btn" onclick="sendQuick('How long do I need to pray?')">How long to pray?</button>
        <button class="qr-btn" onclick="sendQuick('Where is God?')">Where is God?</button>
      </div>`;
    }
    chatWindow.appendChild(div);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  function showTyping() {
    const t = document.createElement('div');
    t.id = 'typing';
    t.className = 'msg bot';
    t.innerHTML = `<div class="typing"><span></span><span></span><span></span></div>`;
    chatWindow.appendChild(t);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }
  function removeTyping() {
    const t = document.getElementById('typing');
    if (t) t.remove();
  }

  function sendMessage() {
    const input = document.getElementById('userInput');
    const text = input.value.trim();
    if (!text) return;
    input.value = '';
    autoResize(input);

    appendMsg(text, 'user');

    const key = text.toLowerCase().trim();
    if (key === 'bye') {
      showTyping();
      setTimeout(() => {
        removeTyping();
        appendMsg('Goodbye! Go and pray. 🙏 May God bless you and keep you.', 'bot');
      }, 900);
      return;
    }

    const reply = responses[key] || "God is your Creator and the creator of the universe. Seek Him with all your heart and you will find Him. 🕊️";
    showTyping();
    setTimeout(() => {
      removeTyping();
      appendMsg(reply, 'bot', true);
    }, 900 + Math.random() * 400);
  }

  function sendQuick(text) {
    document.getElementById('userInput').value = text;
    sendMessage();
  }

  function handleKey(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  function autoResize(el) {
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 100) + 'px';
  }
</script>
</body>
</html>
