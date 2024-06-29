document.addEventListener("DOMContentLoaded", () => {
	const toggleFormLink = document.getElementById("toggleForm");
	const loginForm = document.getElementById("loginForm");
	const registerForm = document.getElementById("registerForm");

	toggleFormLink.addEventListener("click", (event) => {
		event.preventDefault();
		if (loginForm.style.display === "none") {
			loginForm.style.display = "block";
			registerForm.style.display = "none";
			toggleFormLink.textContent = "¿No tienes cuenta? Regístrate aquí";
		} else {
			loginForm.style.display = "none";
			registerForm.style.display = "block";
			toggleFormLink.textContent = "¿Ya tienes una cuenta? Inicia sesión aquí";
		}
	});

	// Validación de formulario de registro
	registerForm.addEventListener("submit", (event) => {
		const password1 = document.getElementById("id_password1").value;
		const password2 = document.getElementById("id_password2").value;
		let valid = true;

		// Reiniciar los mensajes de error
		document.getElementById("password1_error").textContent = "";
		document.getElementById("password2_error").textContent = "";

		// Verificar si las contraseñas son demasiado cortas
		if (password1.length < 8) {
			document.getElementById("password1_error").textContent =
				"La contraseña debe tener al menos 8 caracteres.";
			valid = false;
		}

		// Verificar si las contraseñas coinciden
		if (password1 !== password2) {
			document.getElementById("password2_error").textContent =
				"Las contraseñas no coinciden.";
			valid = false;
		}

		if (!valid) {
			event.preventDefault();
		}
	});
});
