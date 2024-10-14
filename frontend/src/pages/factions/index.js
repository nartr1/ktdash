import React from "react";
import { AspectRatio, Box, Card, Container, Image, LoadingOverlay, SimpleGrid, Text, Title } from "@mantine/core";
import classes from './factions.module.css';
import { Link } from "wouter";
import { useGet } from "../../hooks/use-api";

export default function Factions() {
    const { data: factions, isFetching: isFetchingFactions } = useGet("/faction");
    const cards = factions?.map((faction) => (
        <Card key={faction.factionid} p="md" radius="md" component="a" className={classes.card}>
            <AspectRatio ratio={1920 / 1080}>
                <Image radius="md" src={`https://ktdash.app/img/portraits/${faction.factionid}/${faction.factionid}.jpg`} />
            </AspectRatio>
            <Link href={`/fa/${faction.factionid}`}>
                <Title className={classes.title} mt={5}>{faction.factionname}</Title>
            </Link>
            <Text size="xs" fw={700} mt="md">
                <div dangerouslySetInnerHTML={{ __html: `${faction.description}` }} />
            </Text>
            <Box mt="md">
                <Title order={5}>KT21</Title>
                <SimpleGrid cols={{ base: 2, md: 3 }} spacing={4}>
                    {faction.killteams.filter((team) => team.killteamversion === "kt21").map((kt) => (
                        <Link href={`/fa/${faction.factionid}/kt/${kt.killteamid}`} size="xs" fw={700} mt="md">{kt.killteamname}</Link>))}

                </SimpleGrid>

                <Title mt="md" order={5}>KT24</Title>
                <SimpleGrid cols={{ base: 2, md: 3 }} spacing={4}>
                    {faction.killteams.filter((team) => team.killteamversion === "kt24").map((kt) => (
                        <Link href={`/fa/${faction.factionid}/kt/${kt.killteamid}`} size="xs" fw={700} mt="md">{kt.killteamname}</Link>))}
                </SimpleGrid>
            </Box>
        </Card>
    ));
    if (isFetchingFactions) {
        return (<LoadingOverlay visible={isFetchingFactions} />);
    }

    return (
        <Container py="md" px="md" fluid>
            <SimpleGrid cols={{ base: 1, sm: 2, xl: 3 }}>
                {cards}
            </SimpleGrid>
        </Container>
    );
}
