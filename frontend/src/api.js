const BASE_URL = "http://localhost:5000/api";

export async function fetchUsers() {
  const response = await fetch(`${BASE_URL}/users`);
  return await response.json();
}

export async function logActivity(userId, activity) {
  const response = await fetch(`${BASE_URL}/log_activity`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, activity }),
  });
  return await response.json();
}
