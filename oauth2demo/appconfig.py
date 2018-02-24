class AppConfig():

    """
    URI of Sequencing oAuth2 where you can request user to authorize your app.
    """
    oauth2_authorization_uri = 'https://sequencing.com/oauth2/authorize'

    """
    Sequencing API endpoint.
    """
    api_uri = 'https://api.sequencing.com'

    """
    Redirect URI of your oauth2 app, where it expects Sequencing oAuth2 to
    redirect browser.
    """
    redirect_uri = 'http://localhost:8889/authorize'

    """
    Id of your oauth2 app (oauth2 client).
    You will be able to get this value from Sequencing website.
    """
    client_id = 'SkinnyGenes'

    """
    Secret of your oauth2 app (oauth2 client).
    You will be able to get this value from Sequencing website.
    Keep this value private.
    """
    client_secret = '1orDg2ousKImeDUKuvT-5pIj99dvTEG9Y3DuGdGVEfLmXu4oNr09V8vJPpx28l9EMl9rBdTVXBieViuKYEYfUQ'

    """
    Supply here 'code', which means you want to take 
    the route of authorization code response
    """
    response_type = 'code'

    """
    oAuth2 state.
    It should be some random generated string. State you sent to authorize URI
    must match the state you get, when browser is redirected to the redirect URI
    you provided.
    """
    state = '900150983cd346fb0d6963f7d28e17f72'

    """
    Array of scopes, access to which you request.
    """
    scopes = ['External']
    
    """
    URI of Sequencing oAuth2 where you can obtain access token.
    """
    oauth2_token_uri = 'https://sequencing.com/oauth2/token'

    """
    Supply here 'authorization_code', which means you request to 
    exchange the authorization code for the aouth2 tokens
    """
    grant_type= 'authorization_code' 
