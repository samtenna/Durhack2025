const webAuth = new auth0.WebAuth({
    domain: 'dev-7v3oubna7hezun54.us.auth0.com',
    clientID: '6JMHND7IA8yXWfgbT8YNIDNYzj7eMP5N'
});

async function login(username, password) {
    const res = await webAuth.login({
        realm: 'Username-Password-Authentication',
        username,
        password,
    });
}

async function logout() {
    await webAuth.logout();
}

async function signup(username, password) {
    const res = await webAuth.signup({
        connection: 'Username-Password-Authentication',
        email: username,
        password,
    });
}
