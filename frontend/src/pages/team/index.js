import { useRoute } from "wouter";

export default function Team() {
    const [match, params] = useRoute("/fa/:factionId/kt/:teamId");
    return (
        <>The team page for {params?.teamId}.</>
    );
}
