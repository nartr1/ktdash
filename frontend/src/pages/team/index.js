import { Link, useRoute } from "wouter";
import { useGet } from "../../hooks/use-api";
import { AspectRatio, Box, Card, Container, Flex, Group, Image, LoadingOverlay, SimpleGrid, Stack, Tabs, Text, Title } from "@mantine/core";

export default function Faction() {
    const [match, params] = useRoute("/fa/:factionId/kt/:killteamId");
    const { data: killteam, isFetching: isFetchinigTeam } = useGet(`/killteam?kt=${params?.killteamId}`);
    const teamData = killteam?.[0];
    if (isFetchinigTeam) {
        return (<LoadingOverlay visible={isFetchinigTeam} />);
    }
    if (!teamData) {
        return;
    }
    return (
        <Container py="md" px="md" fluid>
            <Stack>
                <SimpleGrid cols={{ base: 1, sm: 2 }} spacing="md">
                    <Image fit="cover" style={{ objectPosition: "top" }} h={300} radius="md" src={`https://ktdash.app/img/portraits/${params?.factionId}/${params?.killteamId}/${params?.killteamId}.jpg`} />
                    <div justify="flex-start" align="flex-start" grow={1}>
                        <Title>
                            {teamData?.killteamname}
                        </Title>
                        <Text>
                            <div dangerouslySetInnerHTML={{ __html: `${teamData.description}` }} />
                        </Text>
                    </div>
                </SimpleGrid>
                <Tabs defaultValue="operatives">
                    <Tabs.List grow>
                        <Tabs.Tab value="operatives">
                            Operatives
                        </Tabs.Tab>
                        <Tabs.Tab value="ploys">
                            Ploys
                        </Tabs.Tab>
                        <Tabs.Tab value="equipment">
                            Equipment
                        </Tabs.Tab>
                    </Tabs.List>

                    <Tabs.Panel value="operatives">
                        <Box my="md">
                            {teamData?.fireteams?.map((fireteam) => (
                                <>
                                    {!!(teamData?.fireteams?.length > 1) && <Title order={3}>{fireteam.fireteamname}</Title>}
                                    <SimpleGrid mt="md" cols={{ base: 1, md: 2, xl: 3 }} spacing="md">
                                        {fireteam?.operatives?.map((operative) => (
                                            <Card>
                                                <Stack>
                                                    <Title order={3}>{operative.opname}</Title>
                                                    <SimpleGrid cols={{ base: 2 }}>
                                                        <Image fit="cover" style={{ objectPosition: "top" }} h={140} radius="md" src={`https://ktdash.app/img/portraits/${params?.factionId}/${params?.killteamId}/${params?.killteamId}/${operative?.opid}.jpg`} />
                                                        <SimpleGrid mt="md" cols={{ base: 2 }} spacing="md">
                                                            <Flex>APL: {operative.APL}</Flex>
                                                            <Flex>M: {operative.M}</Flex>
                                                            <Flex>SV: {operative.SV}</Flex>
                                                            <Flex>W: {operative.W}</Flex>
                                                        </SimpleGrid>
                                                    </SimpleGrid>
                                                </Stack>
                                            </Card>
                                        ))}
                                    </SimpleGrid>
                                </>
                            ))}
                        </Box>
                    </Tabs.Panel>

                    <Tabs.Panel value="ploys">
                        <SimpleGrid mt="md" cols={{ base: 1, sm: 2 }} spacing="md">
                            <Stack>
                                <Title mx="md" order={2}>Strategic Ploys</Title>
                                {teamData?.ploys?.strat?.map((ploy) => (
                                    <Card>
                                        <Title order={3}>{ploy.ployname}</Title>
                                        <div dangerouslySetInnerHTML={{ __html: `${ploy.description}` }} />
                                    </Card>
                                ))}
                            </Stack>
                            <Stack>
                                <Title mx="md" order={2}>Firefight Ploys</Title>
                                {teamData?.ploys?.tac?.map((ploy) => (
                                    <Card>
                                        <Title order={3}>{ploy.ployname}</Title>
                                        <div dangerouslySetInnerHTML={{ __html: `${ploy.description}` }} />
                                    </Card>
                                ))}
                            </Stack>
                        </SimpleGrid>
                    </Tabs.Panel>
                    <Tabs.Panel value="equipment">
                        Equipment stuff
                    </Tabs.Panel>
                </Tabs>
            </Stack>
        </Container>
    );
}
