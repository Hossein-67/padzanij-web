/**
 * Server state values for a connected server used by padzanij-apiclient.
 */
export const enum ConnectionState {
    SignedIn = 'SignedIn',
    ServerSignIn = 'ServerSignIn',
    ServerSelection = 'ServerSelection',
    ServerUpdateNeeded = 'ServerUpdateNeeded',
    Unavailable = 'Unavailable'
}
