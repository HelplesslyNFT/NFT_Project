import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Sections from '../Enums/Routes';
import Colors from '../Enums/Colors';

export default function RoadMap() {
  const classes = useStyles();

  return (
    <div className={classes.root} id={Sections.ROADMAP}>
     
    </div>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100vh',
    background: Colors.PRIMARY,
  },
}));