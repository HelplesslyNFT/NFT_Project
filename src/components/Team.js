import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Sections from '../Enums/Routes';
import Colors from '../Enums/Colors';

export default function Team() {
  const classes = useStyles();

  return (
    <div className={classes.root} id={Sections.TEAMS}>
     
    </div>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100vh',
    background: Colors.SECONDARY,
  },
}));
