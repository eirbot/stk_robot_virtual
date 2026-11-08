# Export onshape

1. On onshape define a redirect url on `http://localhost:8080/callback` in your application portal
2. Copy the client id and the client secret and fill in them a `.env` like in `.env.example`
3. Set a `SESSION_SECRET_KEY`
5. Run the application: `just serve`
6. Go on `http://localhost:8080`, authenticate and copy the access token
7. Fill in it in your .env
8. Run the export command (TODO: document it)


## Known Limits

A `limit` field has been set in the SDF export config to manage an issue in
`onshape-to-robot`'s handling of continuous DOFs.
