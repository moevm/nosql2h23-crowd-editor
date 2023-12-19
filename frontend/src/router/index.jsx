import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import ProtectedRoute from "./ProtectedProvider";
import Home from "./pages/home";
import Auth from "./pages/auth";
import { AuthProvider } from "./pages/auth/AuthProvider";
import Users from "./pages/users";

export default function Router() {
  const router = createBrowserRouter([
    {
      path: '/auth',
      element: <Auth />
    },
    {
      path: "/",
      element: 
        <ProtectedRoute>
          <Home />
        </ProtectedRoute>
    },
    {
      path: "/users",
      element: 
        <ProtectedRoute>
          <Users />
        </ProtectedRoute>
    },
  ]);

  return (
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
  )
}