import { useRoute } from "wouter";

export default function Team() {
    const [match, params] = useRoute("/fa/:factionId/kt/:teamId");
    console.log(match);
    return (
        <>The team page for {params?.teamId}.</>
    );
}
