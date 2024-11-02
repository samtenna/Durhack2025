const webAuth = new auth0.WebAuth({
    domain: 'dev-7v3oubna7hezun54.us.auth0.com',
    clientID: '6JMHND7IA8yXWfgbT8YNIDNYzj7eMP5N'
});

function login(email, password) {
    webAuth.login({
        realm: 'Username-Password-Authentication',
        email,
        password,
        responseType: 'token id_token',
        redirect_uri: 'http://localhost:5000/',
    }, (e) => {
        if (e) {
            console.error(e);
        } else {
            // redirect
            window.location = "/";
        }
    });
}

async function logout() {
    await webAuth.logout();
}

function register(email, password) {
    webAuth.signup({
        realm: 'Username-Password-Authentication',
        email,
        password,
    }, (e) => {
        if (e) {
            console.error(e);
        } else {
            // redirect
            window.location = "/";
        }
    });
}
