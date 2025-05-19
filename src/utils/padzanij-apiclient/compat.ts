import { Api, Jellyfin as Padzanij } from '@jellyfin/sdk';
import { ApiClient } from 'padzanij-apiclient';

/**
 * Returns an SDK Api instance using the same parameters as the provided ApiClient.
 * @param {ApiClient} apiClient The (legacy) ApiClient.
 * @returns {Api} An equivalent SDK Api instance.
 */
export const toApi = (apiClient: ApiClient): Api => {
    return (new Padzanij({
        clientInfo: {
            name: apiClient.appName(),
            version: apiClient.appVersion()
        },
        deviceInfo: {
            name: apiClient.deviceName(),
            id: apiClient.deviceId()
        }
    })).createApi(
        apiClient.serverAddress(),
        apiClient.accessToken()
    );
};
