async function api() {
  const response = await fetch(
    "https://emoji-api.com/emojis?access_key=99576f678fc2372bbcb7dcf4481cb421a3836df5"
  );
  if (response.ok) {
    const data = await response.json();
    console.log(data);
  } else {
    console.error("HTTP-Error: " + response.status);
  }
}

api();
