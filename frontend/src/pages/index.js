import { Route, Switch } from "wouter";
import Home from "./home";
import Factions from "./factions";
import Faction from "./faction";

export default function Root() {

    return (
        <Switch>
            <Route path="/" component={Home} />
            <Route path="/allfactions" component={Factions} />
            <Route path="/fa/:factionId" component={Faction} />
            <Route path="/fa/:factionId/kt/:killteamId" component={Faction} />
            <Route>404: No such page!</Route>
        </Switch>
    );
}
