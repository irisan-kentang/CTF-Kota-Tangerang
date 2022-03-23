<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Auth;

class DashboardController extends Controller
{
    public function index()
    {
        $flag = "tangerangkota{always_check_your_model_and_request}";
        $isAdmin = Auth::user()->role === 'admin';
        return view('dashboard', [
            'flag' => $flag,
            'isAdmin' => $isAdmin,
        ]);
    }
}
