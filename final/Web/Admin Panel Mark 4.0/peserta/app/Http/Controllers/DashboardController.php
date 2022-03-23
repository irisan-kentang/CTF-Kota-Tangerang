<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Auth;

class DashboardController extends Controller
{
    public function index()
    {
        $flag = "tangerangkota{selamat_tim_anda_mendapatkan_flag______tapi___boong___xixixi}";
        $isAdmin = Auth::user()->role === 'admin';
        return view('dashboard', [
            'flag' => $flag,
            'isAdmin' => $isAdmin,
        ]);
    }
}
