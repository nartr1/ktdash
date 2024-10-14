import { useRoute } from "wouter";

export default function Faction() {
    const [match, params] = useRoute("/fa/:factionId");
    return (
        <>The faction page for {params?.factionId}.</>
    );
}
