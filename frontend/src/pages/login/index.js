import { PasswordInput, Group, Container, TextInput, Stack, Button } from '@mantine/core';
import { useInputState } from '@mantine/hooks';


export default function Login() {
    const [username, setUsername] = useInputState('');
    const [password, setPassword] = useInputState('');

    return (
        <Container py="md">
            <Stack>
                <TextInput
                    value={username}
                    onChange={setUsername}
                    label="Username"
                    placeholder="Username"
                    required
                />
                <PasswordInput
                    value={password}
                    onChange={setPassword}
                    placeholder="Your password"
                    label="Password"
                    required
                />
                <Button>Log In</Button>
            </Stack>
        </Container>
    );
}