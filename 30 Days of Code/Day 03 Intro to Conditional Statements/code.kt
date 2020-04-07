// Written: 07-Apr-2020
// https://www.hackerrank.com/challenges/30-conditional-statements/problem

import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

fun solution(N: Int) {
    when {
        N%2 == 1 -> println("Weird")
        N <= 5 -> println("Not Weird")
        N <= 20 -> println("Weird")
        else -> println("Not Weird")
    }
}

fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)
    val N = scan.nextLine().trim().toInt()

    solution(N)
}
