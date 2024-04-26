import { AppShell, Burger, Group,FileButton, Button, Text, Skeleton, Image, TextInput, NumberInput } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';
import { path } from '@tauri-apps/api';
import { useState, useRef } from 'react';

export function BasicAppShell() {
  const [opened, { toggle }] = useDisclosure();
  const [file, setFile] = useState<File | null>(null);
  const resetRef = useRef<() => void>(null);

  const clearFile = () => {
    setFile(null);
    resetRef.current?.();
  };

  const handleFileChange = (files: FileList | null) => {
    if (files && files.length > 0) {
      setFile(files[0]);
    }
  };


  return (
    <AppShell
      navbar={{ width: 200, breakpoint: 'sm', collapsed: { mobile: !opened } }}
      padding="md"
    >
    
      <AppShell.Navbar p="md">
        

        <Group justify="center">

        <FileButton  resetRef={resetRef} onChange={setFile} accept="image/*">
          {(props) => <Button {...props}>Upload image</Button>}
        </FileButton>

        <Button disabled={!file} color="red" onClick={clearFile}>
          Reset
        </Button>

        <Button variant="filled" size="md">Crop</Button>

        <NumberInput
          size="md"
          placeholder="min"
        />

        <NumberInput
          size="md"
          placeholder="max"
         />

        <Button variant="filled" size="md">Analize</Button>

      </Group>

      {file && (
        <Text size="sm" ta="center" mt="sm">
          Picked file: {file.name}
        </Text>
      )}

      </AppShell.Navbar>
    
      <AppShell.Main>
        
      {file && (
          <img src={URL.createObjectURL(file)} alt="Uploaded image" style={{ maxWidth: '100%' }} />
        )}
        

        </AppShell.Main>
    
    </AppShell>
  );
}

export default BasicAppShell;
