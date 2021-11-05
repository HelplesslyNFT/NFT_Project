import React from 'react';
import { makeStyles } from '@material-ui/core/styles';

import Sections from '../Enums/Routes';
import Colors from '../Enums/Colors';

export default function AboutProject() {
  const classes = useStyles();

  return (
    <div className={classes.root} id={Sections.ABOUT_PROJECT}>
     
    </div>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    height: '100vh',
    background: Colors.SECONDARY,
  },
}));
