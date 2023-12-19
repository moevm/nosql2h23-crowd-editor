import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from './pages/auth/AuthProvider';
import Main from '../components/Main';

export default function ProtectedRoute ({ children }) {
  const { user } = useContext(AuthContext);

  if (!user) {
    return <Navigate to="/auth" replace />;
  }

  return (
    <Main>
      { children }
    </Main>
  );
};
