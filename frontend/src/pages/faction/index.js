import { Link, useRoute } from "wouter";
import { useGet } from "../../hooks/use-api";
import { Container, Image, LoadingOverlay, SimpleGrid, Stack, Text, Title } from "@mantine/core";

export default function Faction() {
    const [match, params] = useRoute("/fa/:factionId");
    const { data: faction, isFetching: isFetchingFaction } = useGet(`/faction?fa=${params?.factionId}`);
    const factionData = faction?.[0];
    if (isFetchingFaction) {
        return (<LoadingOverlay visible={isFetchingFaction} />);
    }
    if (!factionData) {
        return;
    }
    return (
        <Container py="md" px="md" fluid>
            <Stack>
                <SimpleGrid mt="md" cols={{ base: 1, sm: 2 }} spacing="md">
                    <Image fit="cover" style={{ objectPosition: "top" }} h={300} radius="md" src={`https://ktdash.app/img/portraits/${params?.factionId}/${params?.factionId}.jpg`} />
                    <div justify="flex-start" align="flex-start" grow={1}>
                        <Title>
                            {factionData?.factionname}
                        </Title>
                        <Text>
                            <div dangerouslySetInnerHTML={{ __html: `${factionData.description}` }} />
                        </Text>
                    </div>
                </SimpleGrid>
                <Text>
                    <SimpleGrid mt="md" cols={{ base: 2 }} spacing={4}>
                        {factionData?.killteams.map((kt) => (
                            <Link href={`/fa/${factionData.factionid}/kt/${kt.killteamid}`} size="xs" fw={700} mt="md">{kt.killteamname}</Link>))}
                    </SimpleGrid>
                </Text>
            </Stack>
        </Container>
    );
}
