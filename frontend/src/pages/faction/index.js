import { useRoute } from "wouter";
import { useRequest } from "../../hooks/use-api";
import { Card, Container, Image, LoadingOverlay, SimpleGrid, Stack, Tabs, Text, Title } from "@mantine/core";
import classes from './faction.module.css';

export default function Faction() {
    const [, params] = useRoute("/fa/:factionId");
    const { data: faction, isFetching: isFetchingFaction } = useRequest(`/faction?fa=${params?.factionId}`);
    const factionData = faction?.[0];
    if (isFetchingFaction) {
        return (<LoadingOverlay visible={isFetchingFaction} />);
    }
    if (!factionData) {
        return;
    }
    console.log(factionData);
    const cards2021 = factionData.killteams?.filter((killteam) => killteam.killteamversion === "kt21")?.map((killteam) => (
        <Card key={killteam.killteamid} className={classes.card} p="md" radius="md" component="a" href={`/fa/${factionData.factionid}/kt/${killteam.killteamid}`}>
            <Card.Section inheritPadding py="xs">
                <Title order={3}>{killteam.killteamname} (2021)</Title>
            </Card.Section>
            <Image fit="cover" style={{ objectPosition: "top" }} radius="md" src={`/img/portraits/${factionData.factionid}/${killteam.killteamid}/${killteam.killteamid}.jpg`} />
        </Card>
    ));
    const cards2024 = factionData.killteams?.filter((killteam) => killteam.killteamversion === "kt24")?.map((killteam) => (
        <Card key={killteam.killteamid} className={classes.card} p="md" radius="md" component="a" href={`/fa/${factionData.factionid}/kt/${killteam.killteamid}`}>
            <Card.Section inheritPadding py="xs">
                <Title order={3}>{killteam.killteamname} (2024)</Title>
            </Card.Section>
            <Image fit="cover" style={{ objectPosition: "top" }} radius="md" src={`/img/portraits/${factionData.factionid}/${killteam.killteamid}/${killteam.killteamid}.jpg`} />
        </Card>
    ));
    return (
        <Container px="md" pb="md" fluid>
            <Stack>
                <SimpleGrid my="md" cols={{ base: 1, sm: 2 }} spacing="md">
                    <Image fit="cover" style={{ objectPosition: "top" }} h={300} radius="md" src={`/img/portraits/${params?.factionId}/${params?.factionId}.jpg`} />
                    <Stack justify="flex-start" align="flex-start" grow={1}>
                        <Title>
                            {factionData?.factionname}
                        </Title>
                        <Text>
                            <div dangerouslySetInnerHTML={{ __html: `${factionData.description}` }} />
                        </Text>
                    </Stack>
                </SimpleGrid>
                <Tabs defaultValue="kt24">
                    <Stack>
                        <Tabs.List grow>
                            <Tabs.Tab value="kt21">
                                KT2021
                            </Tabs.Tab>
                            <Tabs.Tab value="kt24">
                                KT2024
                            </Tabs.Tab>
                        </Tabs.List>
                        <Tabs.Panel value="kt21">
                            <SimpleGrid cols={{ base: 1, sm: 2, lg: 3, xl: 4 }}>
                                {cards2021}
                            </SimpleGrid>
                        </Tabs.Panel>
                        <Tabs.Panel value="kt24">
                            <SimpleGrid cols={{ base: 1, sm: 2, lg: 3, xl: 4 }}>
                                {cards2024}
                            </SimpleGrid>
                        </Tabs.Panel>
                    </Stack>
                </Tabs>
            </Stack>
        </Container>
    );
}
