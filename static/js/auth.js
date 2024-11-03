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
        redirect_uri: 'https://durhack2025-production.up.railway.app/',
    }, (e, r) => {
        if (e) {
            console.error(e);
        }
        // else {
        //     // redirect
        //     window.location = "/";
        // }
    });
}

function getUser(cb) {
    webAuth.parseHash({ hash: window.location.hash }, (err, authResult) => {
        if (authResult) {
            webAuth.client.userInfo(authResult.accessToken, (err, user) => {
                if (user) {
                    // store in local storage
                    localStorage.setItem('user', JSON.stringify(user));
                    u = user;
                    cb(u);
                    return;
                }

                cb(null);
            });
        } else {
            // check local storage
            const user = localStorage.getItem('user');

            if (user) {
                u = JSON.parse(user);
                cb(u);
                return;
            }

            cb(null);
        }
    });
}

function logout() {
    webAuth.logout();

    // remove from local storage
    localStorage.removeItem('user');
    window.location = "/login";
}

function register(email, password) {
    webAuth.signup({
        connection: 'Username-Password-Authentication',
        email,
        password,
        responseType: 'token id_token',
        redirect_uri: 'https://durhack2025-production.up.railway.app',
    }, (e,) => {
        if (e) {
            console.error(e);
        } else {
            // redirect
            window.location = "/";
        }
    });
}
