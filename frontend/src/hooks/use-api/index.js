import { useLocalStorage } from "@mantine/hooks";
import React from "react";

const API_PATH = "/api";

export function useAPI() {
    const [authToken] = useLocalStorage({ key: 'token' });
    const request = React.useCallback((endpoint, content) => {
        return fetch(`${API_PATH}${endpoint}`, {
            method: "GET",
            ...content,
            headers: {
                ...content?.headers,
                Authorization: authToken ? `Bearer ${authToken}` : undefined
            }
        }).then(response => response.json());
    }, [authToken]);
    return { request }
}

export function useRequest(endpoint, content) {
    const [data, setData] = React.useState(null);
    const [error, setError] = React.useState(null);
    const [isFetching, setIsFetching] = React.useState(false);
    const api = useAPI();
    React.useEffect(() => {
        setIsFetching(true);
        api.request(endpoint, content).then((data) => {
            setData(data);
            setIsFetching(false);
        }).catch((e) => {
            setError(e);
            setIsFetching(false);
        })
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);
    return { data, error, isFetching }
}
