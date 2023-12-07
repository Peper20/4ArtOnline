import * as React from 'react';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import FolderIcon from '@mui/icons-material/Folder';

import ChatIcon from '@mui/icons-material/Chat';
import CollectionsIcon from '@mui/icons-material/Collections';
import FaceIcon from '@mui/icons-material/Face';
export default function BottomNavigationD() {
  const [value, setValue] = React.useState('recents');

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <BottomNavigation  value={value} onChange={handleChange}>
      <BottomNavigationAction
        label="Feed"
        value="feed"
        icon={<ChatIcon />}
      />
      <BottomNavigationAction
        label="Gallery"
        value="gallery"
        icon={<CollectionsIcon />}
      />
      <BottomNavigationAction
        label="Profile"
        value="profile"
        icon={<FaceIcon />}
      />
      <BottomNavigationAction label="Folder" value="folder" icon={<FolderIcon />} />
    </BottomNavigation>
  );
}
