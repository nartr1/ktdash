import React from "react";

const API_PATH = "/api";

export function useAPI() {
    const get = React.useCallback((endpoint) => {
        return fetch(`${API_PATH}${endpoint}`).then(response => response.json());
    }, []);
    const post = React.useCallback((endpoint, body) => {
        return fetch(`${API_PATH}${endpoint}`, {
            method: "POST",
            body: JSON.stringify(body),
        }).then(response => response.json());
    }, []);
    return { get, post }
}

export function useGet(endpoint) {
    const [data, setData] = React.useState(null);
    const [error, setError] = React.useState(null);
    const [isFetching, setIsFetching] = React.useState(false);
    const api = useAPI();
    React.useEffect(() => {
        setIsFetching(true);
        api.get(endpoint).then((data) => {
            setData(data);
            setIsFetching(false);
        }).catch((e) => {
            setError(e);
            setIsFetching(false);
        })
    }, []);
    return { data, error, isFetching }
}

export function usePost(endpoint, body) {
    const [data, setData] = React.useState(null);
    const [error, setError] = React.useState(null);
    const [isFetching, setIsFetching] = React.useState(false);
    const api = useAPI();
    React.useEffect(() => {
        setIsFetching(true);
        api.post(endpoint, body).then((data) => {
            setData(data);
            setIsFetching(false);
        }).catch((e) => {
            setError(e);
            setIsFetching(false);
        })
    }, []);
    return { data, error, isFetching }
}