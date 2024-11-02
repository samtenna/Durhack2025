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

function getUser() {
    let user = null;

    webAuth.parseHash({ hash: window.location.hash }, (err, authResult) => {
        if (authResult) {
            webAuth.client.userInfo(authResult.accessToken, (err, user) => {
                if (user) {
                    // store in local storage
                    localStorage.setItem('user', JSON.stringify(user));
                    return user;
                }
            });
        } else {
            // check local storage
            const user = localStorage.getItem('user');

            if (user) {
                user = JSON.parse(user);
            }

            window.location = "/login";
        }
    });
}

function logout() {
    webAuth.logout();
}

function register(email, password) {
    webAuth.signup({
        connection: 'Username-Password-Authentication',
        email,
        password,
        responseType: 'token id_token',
        redirect_uri: 'http://localhost:5000/',
    }, (e,) => {
        if (e) {
            console.error(e);
        } else {
            // redirect
            window.location = "/";
        }
    });
}
