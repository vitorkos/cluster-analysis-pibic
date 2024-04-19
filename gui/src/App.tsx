import { AppShell, Burger, Group, Skeleton } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';

export function BasicAppShell() {
  const [opened, { toggle }] = useDisclosure();

  return (
    <AppShell
      navbar={{ width: 150, breakpoint: 'sm', collapsed: { mobile: !opened } }}
      padding="md"
    >
    
      <AppShell.Navbar p="md">
        Menu
        {Array(15)
          .fill(0)
          .map((_, index) => (
            <Skeleton key={index} h={28} mt="sm" animate={false} />
          ))}
      </AppShell.Navbar>
    
      <AppShell.Main>
        Main
        </AppShell.Main>
    
    </AppShell>
  );
}

export default BasicAppShell;
