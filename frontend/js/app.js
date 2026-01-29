async function login() {
const res = await fetch("API_GATEWAY_URL/login", {
method: "POST",
body: JSON.stringify({
username: user.value,
password: pass.value
})
});


const data = await res.json();
alert(data.message);
}