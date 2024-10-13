import React from "react";
import factions from '../../assets/factions.json'
import { AspectRatio, Card, Container, Image, SimpleGrid, Text, Title } from "@mantine/core";
import classes from './factions.module.css';
import { Link } from "wouter";

export default function Factions() {
    const cards = factions.map((faction) => (
        <Card key={faction.factionid} p="md" radius="md" component="a" href={`/fa/${faction.factionid}`} className={classes.card}>
            <AspectRatio ratio={1920 / 1080}>
                <Image radius="md" src={`https://ktdash.app/img/portraits/${faction.factionid}/${faction.factionid}.jpg`} />
            </AspectRatio>
            <Title className={classes.title} mt={5}>
                {faction.factionname}
            </Title>
            <Text size="xs" fw={700} mt="md">
                {faction.description}
            </Text>
            <SimpleGrid mt="md" cols={{ base: 1, sm: 2, xl: 3 }}>
                {faction.killteams.map((kt) => (
                    <Link href={`/fa/${faction.factionid}/kt/${kt.killteamid}`} size="xs" fw={700} mt="md">{kt.killteamname}</Link>))}
            </SimpleGrid>
        </Card>
    ));

    return (
        <Container py="md" px="md" fluid>
            <SimpleGrid cols={{ base: 1, sm: 2, xl: 3 }}>{cards}</SimpleGrid>
        </Container>
    );
}
