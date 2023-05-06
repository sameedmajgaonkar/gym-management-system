const messages = document.getElementById("messages");
const input = document.getElementById("input");
const send = document.getElementById("send");
const chat_container = document.getElementById("chatbot");
const data = [{ question: "Hi", answer: "Hello, How are You?" },{question:"What is your name",answer:"My name is AutoBot, Thanks for Asking!"},{ question:"Suggest me a diet Plan",answer:"Are You OverWeight Or UnderWeight?"},{question:"Overweight",answer:"To lose weight, reduce your calorie intake, focus on whole foods, limit processed and high-fat foods, monitor your portion sizes, stay hydrated, exercise regularly, and consider working with a professional for support and accountability." },{question:"Underweight",answer:"To gain weight, increase your calorie intake, focus on nutrient-dense foods, eat frequently, incorporate strength training, stay hydrated, and consider working with a professional for support and accountability."},{question:"How do I improve my health",answer:"Join Our Gym in your vicinity, Our Experienced Trainers provides you the best diet plans and exercises"}];
function sendMessage() {
  const text = input.value.trim(); //remove extra spaces
  if (text.length === 0) {
    return;
  }
  const message = document.createElement("div");
  message.classList.add("message", "user");
  message.textContent = text;
  messages.appendChild(message);
  input.value = "";
  const answer = findAnswer(data, text);
  displayAnswer(answer);
}
function findAnswer(data, text) {
  for (let i = 0; i < data.length; i++) {
    const question = data[i].question.toLowerCase();
    if (text.toLowerCase().includes(question)) {
      return data[i].answer;
    }
  }
  return "Sorry I didn't Understand ! Please Try Again";
}

function displayAnswer(answer) {
  const message = document.createElement("div");
  message.classList.add("message", "bot");
  message.textContent = answer;
  messages.appendChild(message);
  const utterance = new SpeechSynthesisUtterance(answer);
  utterance.voice = speechSynthesis.getVoices()[1];
  speechSynthesis.speak(utterance);
  chat_container.scrollTop = chat_container.scrollHeight;
}

send.addEventListener("click", sendMessage);
input.addEventListener("keydown", (event) => {
  if (event.key == "Enter") {
    sendMessage();
  }
});
