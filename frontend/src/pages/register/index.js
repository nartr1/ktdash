import { PasswordInput, Group, Container, TextInput, Stack, Button } from '@mantine/core';
import { useInputState } from '@mantine/hooks';


export default function Register() {
    const [username, setUsername] = useInputState('');
    const [password, setPassword] = useInputState('');
    const [password2, setPassword2] = useInputState('');

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
                <PasswordInput
                    value={password2}
                    onChange={setPassword2}
                    placeholder="Confirm Password"
                    label="Confirm Password"
                    required
                />
                <Button>Sign Up</Button>
            </Stack>
        </Container>
    );
}