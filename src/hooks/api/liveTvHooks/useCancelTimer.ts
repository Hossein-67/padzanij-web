import type { LiveTvApiCancelTimerRequest } from '@jellyfin/sdk/lib/generated-client';
import { getLiveTvApi } from '@jellyfin/sdk/lib/utils/api/live-tv-api';
import { useMutation } from '@tanstack/react-query';
import { type PadzanijApiContext, useApi } from 'hooks/useApi';

const cancelTimer = async (
    apiContext: PadzanijApiContext,
    params: LiveTvApiCancelTimerRequest
) => {
    const { api } = apiContext;

    if (!api) throw new Error('[cancelTimer] No API instance available');

    const response = await getLiveTvApi(api).cancelTimer(params);
    return response.data;
};

export const useCancelTimer = () => {
    const apiContext = useApi();
    return useMutation({
        mutationFn: (params: LiveTvApiCancelTimerRequest) =>
            cancelTimer(apiContext, params)
    });
};
