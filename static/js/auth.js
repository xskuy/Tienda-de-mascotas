document.addEventListener("DOMContentLoaded", () => {
	const loginForm = document.getElementById("loginForm");
	const registerForm = document.getElementById("registerForm");
	const toggleForm = document.getElementById("toggleForm");
	const formTitle = document.getElementById("formTitle");

	toggleForm.addEventListener("click", (e) => {
		e.preventDefault();
		if (loginForm.style.display === "none") {
			loginForm.style.display = "block";
			registerForm.style.display = "none";
			toggleForm.textContent = "¿No tienes cuenta? Regístrate aquí";
			formTitle.textContent = "Login";
		} else {
			loginForm.style.display = "none";
			registerForm.style.display = "block";
			toggleForm.textContent = "¿Ya tienes cuenta? Inicia sesión aquí";
			formTitle.textContent = "Registro";
		}
	});
});
